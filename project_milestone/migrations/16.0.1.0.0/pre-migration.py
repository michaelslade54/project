from openupgradelib import openupgrade

xml_ids = ["view_task_enhancement_milestone_tree",
           "view_task_enhancement_milestone_form",
           "quick_create_task_form",
           "view_task_enhancement_milestone_kanban",
           "view_task_enhancement_gantt",
           "view_task_enhancement_search_milestone_form",
           "project_milestone_seq",
           "project_milestone_view_list",
           "project_milestone_view_form",
           "project_milestone_view_search",
           "project_milestone_action",
           "project_milestone_view_inherit_list",
           "project_enhancement_milestone_view_inherit_form",
           "project_enhancement_milestone_view_inherit_simple",
           "project_enhancements_milestone_inherit_search_view",
           ]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)