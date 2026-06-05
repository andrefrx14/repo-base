# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[CONCLUÍDA]" if task["done"] else "[ABERTA]"
    return f"{status} | Tarefa: {task['title']} | Prioridade: P{task['priority']} | ID:{task['id']}"

def filter_tasks(tasks, show_done=True, min_priority=None):
    if not show_done:
        tasks = [t for t in tasks if not t["done"]]

    if min_priority is not None:
        tasks = [t for t in tasks if t["priority"] >= min_priority]

    return tasks