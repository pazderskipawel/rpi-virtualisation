# rpi-automation-services-n8n

n8n automation configs for services running on raspberry pi

* `[n8n]export_workflows_as_json.json` - this is saving all not archived workflows into separate files
* `[n8n][old]export_workflows_as_json_old_sh_version.json` - old version of above - it was using bash commands instaed of api call so it ws executing much longer
* `[n8n]get_current_credentials.json` - allows to see all current unencrypted credentias stored in n8n
* `[git]sync_n8n_workflows.json` - synchronises current workflows in repo
synchronising workflows will be done by n8n, for now it's made manually so repo is not empty

### How to import workflows to n8n (cli)
[DOCS](https://docs.n8n.io/hosting/cli-commands/#workflows_1)

Import workflows from a specific file:
```
n8n import:workflow --input=file.json
```
Import all the workflow files as JSON from the specified directory:
```
n8n import:workflow --separate --input=backups/latest/
```