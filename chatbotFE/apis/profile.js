const BASE_URL = "http://127.0.0.1:5000";

export async function createProfile(profile) {
  return axios.post(`${BASE_URL}/api/matcher/profile`, profile);
}

export async function getRandomProfile() {
  return axios.get(`${BASE_URL}/api/matcher/random-profile`);
}
