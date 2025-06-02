import { renderProfileForm } from "./components/ProfileForm.js";
import { renderRandomProfile } from "./components/RandomProfileCard.js";
import { renderSurvey } from "./components/SurveyForm.js";
import { fetchSurveyQuestions } from './apis/survey.js';

renderProfileForm(document.getElementById("formSection"));
renderRandomProfile(document.getElementById("randomSection"));

const surveyContainer = document.getElementById("survey-container");

fetchSurveyQuestions().then(data => {
  window.surveyQuestions = data;
  renderSurvey(surveyContainer);
});

