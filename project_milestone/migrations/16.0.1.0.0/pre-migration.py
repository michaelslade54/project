from openupgradelib import openupgrade

field_spec = [
    ("project.milestone", "project_milestone", "project_task_ids", "task_ids"),
    ("project.milestone", "project_milestone", "target_date", "deadline"),    
]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, field_spec, False)
    