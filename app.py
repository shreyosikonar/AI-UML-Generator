from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from model.uml_extractor import extract_uml_components
from model.relationship_classifier import classify_relationships
from utils.confidence_score import generate_confidence
from utils.preprocessing import preprocess_text

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def generate(request: Request, srs_text: str = Form(...)):
    cleaned_text = preprocess_text(srs_text)
    components = extract_uml_components(cleaned_text)
    relationships = classify_relationships(components)
    confidence = generate_confidence(components)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "components": components,
        "relationships": relationships,
        "confidence": confidence
    })