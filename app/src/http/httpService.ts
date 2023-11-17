// httpService.ts
import axios, { AxiosInstance } from 'axios';
import { Md5 } from 'ts-md5';

class HttpService {
  private axiosInstance: AxiosInstance;

  constructor() {
    let createData = {
      baseURL: 'https://your-api-url.com', // 你的基础 API URL
      headers: {
        'Content-Type': 'application/json'
      }
    }
    createData.baseURL = "http://8.222.188.249:8000";
    this.axiosInstance = axios.create(createData);
  }

  public setToken(token: string): void {
    this.axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  }

  public async login(username: string, password: string): Promise<any> {
    const md5 = new Md5();
    const passwordMd = md5.appendStr(password).end();
    try {
      const response = await this.axiosInstance.post('/api/user/login', {
        "email": username,
        "password": passwordMd
      });
      return response.data;
    } catch (error) {
      // 错误处理
      throw error;
    }
  }

  // 其他 API 方法...
}

export const httpService = new HttpService();
