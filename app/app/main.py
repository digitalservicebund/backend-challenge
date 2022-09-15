"""dsb.app.main."""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app import config
from app.services.department import aggregate_dataset_counts_by_ministry
from app.services.utils import read_departments_json
from app.services.govdata import get_department_metadata


def init_app() -> FastAPI:
    """Init application"""
    return FastAPI()


app = init_app()
templates = Jinja2Templates(directory=config.TEMPLATES_DIR)


@app.get('/', response_class=HTMLResponse)
def get_department_with_dataset_counts(request: Request):
    # read departments.json
    departments_with_subordinates = read_departments_json()
    # get all department metadata from GovData CKAN API
    all_department_metadata = get_department_metadata()
    aggregated_counts_desc = aggregate_dataset_counts_by_ministry(all_department_metadata,
                                                                  departments_with_subordinates)
    return templates.TemplateResponse('departments.html', {'departments': aggregated_counts_desc, 'request': request})
