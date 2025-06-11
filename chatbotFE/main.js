import { renderProfileForm } from "./components/ProfileForm.js";
import { renderRandomProfile } from "./components/RandomProfileCard.js";
import { fetchSurveyQuestions } from './apis/survey.js';
import { renderSurvey } from "./components/surveyForm.js";

renderProfileForm(document.getElementById("formSection"));
renderRandomProfile(document.getElementById("randomSection"));

const surveyContainer = document.getElementById("survey-container");

fetchSurveyQuestions().then(data => {
  window.surveyQuestions = data;
  renderSurvey(surveyContainer);
});

