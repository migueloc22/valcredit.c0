const API_URL = import.meta.env.VITE_API_URL;
import axios from "axios";
export const get = async (url) => {
  try {
    const response = await axios.get(`${API_URL}${url}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export const post = async (url, data) => {
  try {
    const response = await axios.post(`${API_URL}${url}`, data);
    return response.data;
  } catch (error) {
    console.error("Error posting data:", error);
    throw error;
  }
};
export const put = async (url, data) => {
  try {
    const response = await axios.put(`${API_URL}${url}`, data);
    return response.data;
  } catch (error) {
    console.error("Error updating data:", error);
    throw error;
  }
};
export const del = async (url) => {
  try {
    const response = await axios.delete(`${API_URL}${url}`);
    return response.data;
  } catch (error) {
    console.error("Error deleting data:", error);
    throw error;
  }
};
