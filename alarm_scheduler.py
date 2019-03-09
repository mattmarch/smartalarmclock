import sys, os
import datetime

from crontab import CronTab

from AlarmState import AlarmState

JOB_COMMENT = 'Scheduled Wake Up'
WAKE_UP_SCRIPT_NAME = 'wake_up.py'
VENV_PYTHON = 'venv/bin/python'


def get_cron_command():
    current_dir_path = sys.path[0]
    script_path = os.path.join(current_dir_path, WAKE_UP_SCRIPT_NAME)
    python_path = os.path.join(current_dir_path, VENV_PYTHON)
    return f'{python_path} {script_path} >> ~/alarmCronLog.txt'


def update_job(enabled: bool, time: datetime.time):
    cron = CronTab(user=True)

    job = get_job_and_clean_duplicates(cron)
    if job is None:
        # create job if it doesn't exist
        job = cron.new(command=get_cron_command(), comment=JOB_COMMENT)
    job.enable(enabled)
    job.setall(time)
    cron.write()


def get_state():
    cron = CronTab(user=True)
    job = get_job_and_clean_duplicates(cron)
    if job is None:
        return None
    return AlarmState(daily_job_to_time(job), job.enabled)


def get_job_and_clean_duplicates(cron):
    jobs = cron.find_comment(JOB_COMMENT)
    # return first job and remove the rest
    job_to_return = None
    for i, job in enumerate(jobs):
        if i == 0:
            job_to_return = job
        else:
            cron.remove(job)
    cron.write()
    return job_to_return


def daily_job_to_time(job):
    hour = int(str(job.hour))
    minute = int(str(job.minute))
    return datetime.time(hour, minute, 0)
            