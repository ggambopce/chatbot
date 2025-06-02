import { submitSurveyApi } from "../apis/survey.js";

export function renderSurvey(container) {

    container.innerHTML = "";
    
  const surveyQuestions = window.surveyQuestions || [];

  surveyQuestions.forEach((q) => {
    
    const box = document.createElement("div");
    box.className = "question-box";

    const title = document.createElement("h3");
    title.textContent = `${q.number}. ${q.text}`;
    box.appendChild(title);

    q.answers.forEach((a) => {
      const label = document.createElement("label");
      label.style.display = "block";

      const radio = document.createElement("input");
      radio.type = "radio";
      radio.name = `question-${q.id}`;
      radio.value = a.id;

      label.appendChild(radio);
      label.append(` ${a.text}`);
      box.appendChild(label);
    });

    container.appendChild(box);
  });

  const submitBtn = document.createElement("button");
  submitBtn.textContent = "제출하기";
  submitBtn.onclick = handleSubmit;
  container.appendChild(submitBtn);
}

function handleSubmit() {
  const user_id = prompt("사용자 ID를 입력하세요");
  const answers = [];

  window.surveyQuestions.forEach((q) => {
    const selected = document.querySelector(`input[name='question-${q.id}']:checked`);
    if (selected) {
      answers.push({ question_id: q.id, answer_id: parseInt(selected.value) });
    }
  });

  if (answers.length !== window.surveyQuestions.length) {
    alert("모든 질문에 응답해주세요.");
    return;
  }

  submitSurveyApi(user_id, answers)
    .then((res) => {
      alert(`분석 결과: ${res.inferred_type}`);
      console.log("분석 상세:", res);
    })
    .catch((err) => {
      console.error("설문 제출 실패", err);
    });
}
