// httpService.ts
import axios, { AxiosInstance } from 'axios';
import { Md5 } from 'ts-md5';

class HttpService {
  private axiosInstance: AxiosInstance;

  constructor() {
    let createData = {
      baseURL: '', // 你的基础 API URL
      headers: {
        'Content-Type': 'application/json'
      }
    }
    // createData.baseURL = "http://8.222.188.249:8000";
    // createData.baseURL = "https://myswap-api.where22fun.com";
    this.axiosInstance = axios.create(createData);
    localStorage.getItem('token') && this.setToken(localStorage.getItem('token')!);
  }

  public setToken(token: string): void {
    this.axiosInstance.defaults.headers.common['Authorization'] = `bearer ${token}`;
    this.axiosInstance.defaults.headers.common['token'] = token;
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

  public async getAllMoney(): Promise<number> {
    // const accountBalance = await this.axiosInstance.get('/api/okx/account/balance');
    // const fundingBalance = await this.axiosInstance.get('/api/okx/funding/balance');
    // const fundingValuation = await this.axiosInstance.get('/api/okx/funding/valuation');
    // const earningOffers = await this.axiosInstance.get('/api/okx/earning/offers');
    // const earningOrderActive = await this.axiosInstance.get('/api/okx/earning/orders-active');
    // const fundingSavingBalance = await this.axiosInstance.get('/api/okx/funding/saving-balance');
    const res = await this.axiosInstance.get('/api/okx/funding/valuation');
    let allMoney = 0;
    if (!res.data.data) {
      return -1;
    }
    res.data.data.forEach((element: any) => {
      allMoney += Number(element.totalBal);
    });
    return allMoney;
  }

  public async checkToken(token: string): Promise<boolean> {
    const data = await this.axiosInstance.get('/api/user/check?token=' + token);
    if (data.data.code == 200) {
      return true;
    }
    return false;
  }

  // 其他 API 方法...
}

export const httpService = new HttpService();
