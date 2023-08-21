from openupgradelib import openupgrade

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(env.cr, [('project_category','project_type')],False)