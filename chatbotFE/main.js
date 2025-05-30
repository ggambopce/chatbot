import { renderProfileForm } from "./components/ProfileForm.js";
import { renderRandomProfile } from "./components/RandomProfileCard.js";

document.addEventListener("DOMContentLoaded", () => {
  renderProfileForm(document.getElementById("formSection"));
  renderRandomProfile(document.getElementById("randomSection"));
});