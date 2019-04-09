import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http: HttpClient) {
  }
  getDemoRegression(): Observable<any> {
    return this.http.get(this.baseurl + '/regression_demo_info/',
      {headers: this.httpHeaders});
  }
  getDemoDnn(): Observable<any> {
    return this.http.get(this.baseurl + '/dnn_demo_info/',
      {headers: this.httpHeaders});
  }
  getRegression(): Observable<any> {
    return this.http.get(this.baseurl + '/regression_info/',
      {headers: this.httpHeaders});
  }
  getDnn(): Observable<any> {
    return this.http.get(this.baseurl + '/dnn_info/',
      {headers: this.httpHeaders});
  }

  getPolynomial(): Observable<any> {
    return this.http.get(this.baseurl + '/poly_info/',
      {headers: this.httpHeaders});
  }

  getLogistical(): Observable<any> {
    return this.http.get(this.baseurl + '/log_info/',
      {headers: this.httpHeaders});
  }
  getMovingAverages(): Observable<any> {
    return this.http.get(this.baseurl + '/simple_ma_info/',
      {headers: this.httpHeaders});
  }
}
