const BASE_URL = "http://127.0.0.1:5000";

export async function submitSurveyApi(user_id, answers) {
  const res = await axios.post(`${BASE_URL}/survey/submit`, {
    user_id,
    answers
  });
  return res.data;
}

export async function fetchSurveyQuestions() {
  const res = await axios.get(`${BASE_URL}/survey/questions`);
  return res.data;
}
