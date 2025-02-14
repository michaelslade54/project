from odoo.upgrade import util

def migrate(cr, version):
    task_obj = util.env(cr)["project.task"]
    sequence_obj = util.env(cr)["ir.sequence"]
    tasks = task_obj.search([('code','=',False)], order="id")
    for task_id in tasks.ids:
        cr.execute(
            "UPDATE project_task SET code = %s WHERE id = %s;",
            (
                sequence_obj.next_by_code("project.task"),
                task_id,
            ),
        )