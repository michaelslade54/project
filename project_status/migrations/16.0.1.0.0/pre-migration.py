from openupgradelib import openupgrade

xml_ids = ["project_status.project_status_view_list",
           "project_status.project_status_action",
           "project_status.view_project",
           "project_status.edit_project",
           "project_status.project_project_view_form_simplified",
           "project_status.project_view_kanban",
           "project_status.view_project_project_filter",
           
           ]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)
    #  Create all the project stages, use the same ids to make it easier to copy.
    env.cr.execute(
        """
        INSERT INTO project_project_stage(id, name, sequence, fold)
        SELECT id, name, status_sequence, fold FROM project_status;
        """
    )

    # Set the project stages to the old project statuses
    env.cr.execute(
        """
        UPDATE project_project
        SET stage_id = project_status;
        """
    )