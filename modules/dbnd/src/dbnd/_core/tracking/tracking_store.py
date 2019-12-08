import logging
import typing


if typing.TYPE_CHECKING:
    from typing import List

    from targets.base_target import Target
    from targets.metrics.target_value_metrics import ValueMetrics

    from dbnd.api.tracking_api import InitRunArgs
    from dbnd._core.task_run.task_run import TaskRun
    from dbnd._core.run.databand_run import DatabandRun

logger = logging.getLogger(__name__)


class TrackingStore(object):
    @staticmethod
    def _serialize_dbnd_objects(dbnd_run):
        # type: (DatabandRun) -> InitRunArgs
        from dbnd._core.tracking.tracking_info_convertor import TrackingInfoBuilder

        init_run_args = TrackingInfoBuilder(dbnd_run).build_init_args()
        return init_run_args

    def init_scheduled_job(self, scheduled_job):
        pass

    def init_run(self, run):
        # type: (DatabandRun) -> List[int]
        pass

    def set_run_state(self, run, state, timestamp=None):
        pass

    def set_task_reused(self, task_run):
        pass

    def set_task_run_state(self, task_run, state, error=None, timestamp=None):
        pass

    def set_task_run_states(self, task_runs):
        pass

    def save_task_run_log(self, task_run, log_body):
        pass

    def save_external_links(self, task_run, external_links_dict):
        pass

    def log_target_metrics(self, task_run, target, value_metrics):
        # type: (TaskRun, Target, ValueMetrics) -> None
        pass

    def log_metric(self, task_run, metric):
        pass

    def log_artifact(self, task_run, name, artifact, artifact_target):
        pass

    def add_task_runs(self, run, task_runs):
        pass

    def setup_and_validation(self, databand_version):
        pass

    def heartbeat(self, run_uid):
        pass


class CompositeTrackingStore(TrackingStore):
    def __init__(self, stores):
        self._stores = stores

    def _invoke(self, name, kwargs):
        for store in self._stores:
            try:
                handler = getattr(store, name)
                handler(**kwargs)
            except Exception as ex:
                logger.exception(
                    "Failed to store tracking information from %s at %s"
                    % (name, store.__class__.__name__)
                )
                raise

    def init_run(self, **kwargs):
        return self._invoke(CompositeTrackingStore.init_run.__name__, kwargs)

    def set_run_state(self, **kwargs):
        return self._invoke(CompositeTrackingStore.set_run_state.__name__, kwargs)

    def set_task_reused(self, **kwargs):
        return self._invoke(CompositeTrackingStore.set_task_reused.__name__, kwargs)

    def set_task_run_state(self, **kwargs):
        return self._invoke(CompositeTrackingStore.set_task_run_state.__name__, kwargs)

    def set_task_run_states(self, **kwargs):
        return self._invoke(CompositeTrackingStore.set_task_run_states.__name__, kwargs)

    def save_task_run_log(self, **kwargs):
        return self._invoke(CompositeTrackingStore.save_task_run_log.__name__, kwargs)

    def save_external_links(self, **kwargs):
        return self._invoke(CompositeTrackingStore.save_external_links.__name__, kwargs)

    def log_target_metrics(self, **kwargs):
        return self._invoke(CompositeTrackingStore.log_target_metrics.__name__, kwargs)

    def log_metric(self, **kwargs):
        return self._invoke(CompositeTrackingStore.log_metric.__name__, kwargs)

    def log_artifact(self, **kwargs):
        return self._invoke(CompositeTrackingStore.log_artifact.__name__, kwargs)

    def close(self):
        pass

    def add_task_runs(self, **kwargs):
        return self._invoke(CompositeTrackingStore.add_task_runs.__name__, kwargs)

    def setup_and_validation(self, **kwargs):
        return self._invoke(
            CompositeTrackingStore.setup_and_validation.__name__, kwargs
        )

    def heartbeat(self, **kwargs):
        return self._invoke(CompositeTrackingStore.heartbeat.__name__, kwargs)
