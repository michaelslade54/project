from openupgradelib import openupgrade

xml_ids = ["project_milestone.view_task_enhancement_milestone_tree",
           "project_milestone.view_task_enhancement_milestone_form",
           "project_milestone.quick_create_task_form",
           "project_milestone.view_task_enhancement_milestone_kanban",
           "project_milestone.view_task_enhancement_gantt",
           "project_milestone.view_task_enhancement_search_milestone_form",
           "project_milestone.project_milestone_seq",
           "project_milestone.project_milestone_view_list",
           "project_milestone.project_milestone_view_form",
           "project_milestone.project_milestone_view_search",
           "project_milestone.project_milestone_action",
           "project_milestone.project_milestone_view_inherit_list",
           "project_milestone.project_enhancement_milestone_view_inherit_form",
           "project_milestone.project_enhancement_milestone_view_inherit_simple",
           "project_milestone.project_enhancements_milestone_inherit_search_view",
           ]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)