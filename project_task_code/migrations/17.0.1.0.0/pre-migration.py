from openupgradelib import openupgrade

import logging

_logger = logging.getLogger(__name__)

@openupgrade.migrate()
def migrate(env, version):
    
    task_obj = env["project.task"]
    sequence_obj = env["ir.sequence"]
    tasks = task_obj.search([('code','=',False)], order="id")
    for task_id in tasks.ids:
        env.cr.execute(
            "UPDATE project_task SET code = %s WHERE id = %s;",
            (
                sequence_obj.next_by_code("project.task"),
                task_id,
            ),
        )
        _logger.warning("ID CHANGED: " + str(task_id))