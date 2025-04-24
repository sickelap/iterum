## Stack used:
- Django
- SQLite
- TailwindCSS
- Tabler icons

## Design choices:
- separate applications for:
  - data models and admin (business logic)
  - templates (woth views) for UI
  - theme for styling
- reusable components (template tags) for more concise templates
- explicitly failing to start if no SECRET_KEY provided in environment
- for this task SQLite is enough, changing to Postgres is matter of replacing connection string in config (did not configure to use env)
- chose HTMX for displaying popup. Works well with Django
- because page requires user to be shown I decided to use django login feature

## Assumptions
I am pretty sure that I don't understand the busines details behind data modeling so I went as such:
- location is defined by address
- location can have many appliances
- appliance that is assigned to location should not appear in inventory
- inventory of appliances contains all appliances that don't have location
- not sure what should be the calculation of matching score. now value is random
- could be I am wrong with my assumptions but I was not sure what cost represent, wether it's a cost of appliance or proce + maintenance over time? should the energy cost be added too> if cost is combination of price with maintenance then there should be a price field and a audit log for all maintenance events with timestamps and cost.

## Caveats
- in order to run in dev, need to spin django server and tailwind separately:
  - manage.py runserver in one terminal
  - manage.py tailwind start in another
- did not spend time to prepare dev environment using docker compose as thought I won't have enough time
- because of time constraints did not finish popup design and creating order. Added comments.
- no calculation of warranty expiration is done in implementation

## Running locally

```bash
cp .env.sample .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata data.json
./manage.py runserver
```

Create superuser with `manage.py createsuperuser`

data.json contains fixture of first user jordan:jordan
