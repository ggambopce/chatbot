import { getRandomProfile } from "../apis/profile.js";

export function renderRandomProfile(container) {
  container.innerHTML = `<button id="randomBtn">랜덤 프로필 보기</button><div id="profileResult"></div>`;

  document.getElementById("randomBtn").addEventListener("click", async () => {
    const res = await getRandomProfile();
    const p = res.data;
    document.getElementById("profileResult").innerHTML = `
      <h3>${p.nickname} (${p.age})</h3>
        <p><strong>성별:</strong> ${p.gender}</p>
        <p><strong>자기소개:</strong> ${p.bio}</p>
        <img src="${p.image_url}" alt="프로필 이미지" width="150" />
        <p style="font-size:12px; color:gray;">등록일: ${new Date(p.created_at).toLocaleString()}</p>
    `;
  });
}
