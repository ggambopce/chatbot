import { createProfile } from "../apis/profile.js";

export function renderProfileForm(container) {
  container.innerHTML = `
    <form id="profileForm">
      <input name="nickname" placeholder="별명" required />
      <input name="age" placeholder="생년월일 (예: 2000-05-30)" required />
      <input name="gender" placeholder="성별 (예: female)" required />
      <input name="bio" placeholder="자기소개" />
      <input name="image_url" placeholder="이미지 URL" required />
      <input name="user_name" placeholder="이름 (수락 후 공개)" />
      <input name="phone_number" placeholder="전화번호 (수락 후 공개)" />
      <input name="sns_link" placeholder="SNS 링크 (수락 후 공개)" />
      <button type="submit">제출</button>
    </form>
  `;

  document.getElementById("profileForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    await createProfile(data);
    alert("프로필이 등록되었습니다");
  });
}
