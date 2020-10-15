from typing import Dict, List

from dbnd import parameter
from dbnd._core.task import Config


class AirflowMonitorConfig(Config):

    _conf__task_family = "airflow_monitor"

    interval = parameter(
        default=10, description="Sleep time (in seconds) between fetches when not busy"
    )[int]

    dag_ids = parameter(default=None, description="Specific DAGs to monitor")[List[str]]

    include_logs = parameter(default=False)[bool]

    include_task_args = parameter(
        default=False, description="Include all task arguments when fetching task data."
    )[bool]

    include_xcom = parameter(
        default=False, description="Include all task xcom dictionary"
    )[bool]

    fetcher = parameter(
        default="web",
        description="Options: web, db, composer. web - uses the export plugin api, db - connects directly to AF DB.",
    )[str]

    tasks_per_fetch = parameter(
        default=None, description="Max number of tasks to retrieve at each fetch"
    )[int]

    airflow_url = parameter(default=None)[str]

    airflow_external_url = parameter(default=None)[str]

    composer_client_id = parameter(default=None)[str]

    # Used by db fetcher
    local_dag_folder = parameter(default=None)[str]

    sql_alchemy_conn = parameter(default=None, description="db url")[str]

    rbac_enabled = parameter(
        default=True, description="Is rbac mode enabled in the server"
    )[str]

    rbac_username = parameter(
        default={},
        description="Username credentials to use when monitoring airflow with rbac enabled",
    )[str]

    rbac_password = parameter(
        default={},
        description="Password credentials to use when monitoring airflow with rbac enabled",
    )[str]

    use_experimental_api = parameter(
        default=False,
        description="Use export data api from via airflow experimental api. When false, web fetcher will use flask regular api",
    )

    # Used by file fetcher
    json_file_path = parameter(
        default=None, description="A json file to be read ExportData information from"
    )[str]

    operator_user_kwargs = parameter(
        default=[],
        description="Control which task arguments should be treated as user instead of system",
    )[Dict[str, List[str]]]

    debug_sync_log_dir_path = parameter(default=None)[str]

    allow_duplicates = parameter(default=False)[bool]

    rbac_username = parameter(
        default={},
        description="Username credentials to use when monitoring airflow with rbac enabled",
    )[str]

    rbac_password = parameter(
        default={},
        description="Password credentials to use when monitoring airflow with rbac enabled",
    )[str]