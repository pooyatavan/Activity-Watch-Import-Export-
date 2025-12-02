from aw_client import ActivityWatchClient
import os, requests, enum

class MSG(enum.Enum):
    impj = 'Importing {lenfile} JSON files to ActivityWatch...'
    Erdir = 'Error: Directory {directory} does not exist!'
    impsuc = 'Success: File imported {filename}'
    impsuce = 'Success: File imported {filename} with {events_count} events imported'
    comp = 'COMPLETE! Total files processed: {lenfile}'
    view = 'View in ActivityWatch: http://localhost:5600/#/buckets'
    er = 'AW Server not run'
    dbucket = 'Deleted: {bucket}'
    fbucket = 'Failed {bucket}: {e}"'
    process = 'Processing: {filename}'

username = os.environ.get('USERNAME')
directory = f"C:\\Users\\{username}\\OneDrive"
aw_import_url = "http://localhost:5600/api/0/import"
json_files = [f for f in os.listdir(directory) if f.lower().endswith('.json')]
auth_file = f"C:\\Users\\{username}\\AppData\\Roaming\\aw-client\\auth"

def update():
    print(MSG.impj.value.format(lenfile=len(json_files)))
    if not os.path.exists(directory):
        print(MSG.Erdir.value.format(directory=directory))
        return
    total_events = 0
    for filename in json_files:
        full_path = os.path.join(directory, filename)
        print(MSG.process.value.format(filename=filename))
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                body = f.read()
            response = requests.post(aw_import_url, data=body.encode("utf-8"), headers={"Content-Type": "application/json"},)
            response.raise_for_status()
            try:
                resp_json = response.json()
            except ValueError:
                resp_json = None 
            if isinstance(resp_json, dict) and "events" in resp_json:
                events_count = len(resp_json["events"])
                total_events += events_count
                print(MSG.impsuce.value.format(filename=filename, events_count=events_count))
            else:
                print(MSG.impsuc.value.format(filename=filename))
        except Exception as e:
            print(f"   Error: {e}")
    print(MSG.comp.value.format(lenfile=len(json_files)))
    print(MSG.view.value)

def delete():
    if os.path.exists(auth_file):
        with open(auth_file, 'r') as f:
            auth_line = f.read().strip()
            os.environ['AW_CLIENT_AUTH'] = auth_line
    client = ActivityWatchClient('deleter')
    try:
        buckets = client.get_buckets()
        for bucket_id in list(buckets.keys()):
            try:
                client.delete_bucket(bucket_id, force=True)
                print(MSG.dbucket.value.format(bucket=bucket_id))
            except Exception as e:
                print(MSG.fbucket.value.format(bucket=bucket_id, e=e))
    except:
        print(MSG.er.value)

delete()
update()
