from app.models import Task


def register_task(task):
    Task.objects.create(title=task.title, description=task.description,
                        expiration_date=task.expiration_date,
                        priority=task.priority, user=task.user)


def task_list(user):
    return Task.objects.filter(user=user).all()
    # com esse filter, só traz os referentes ao usuario
    # é um SELECT * FROM app_task


def task_list_id(id):
    return Task.objects.get(id=id)


def edit_task(task_db, new_task):
    task_db.title = new_task.title
    task_db.description = new_task.description
    task_db.expiration_date = new_task.expiration_date
    task_db.priority = new_task.priority

    task_db.save(force_update=True)


def remove_task(task_db):
    task_db.delete()
