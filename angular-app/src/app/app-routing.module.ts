import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {MainPageComponent} from './components/main-page/main-page.component';
import {RegChartComponent} from './components/reg-chart/reg-chart.component';
import {RegDnnComponent} from './components/reg-dnn/reg-dnn.component';
import {PolynRegComponent} from "./components/polyn-reg/polyn-reg.component";
import {LogRegComponent} from "./components/log-reg/log-reg.component";
import {MovAvgComponent} from "./components/mov-avg/mov-avg.component";

const routes: Routes = [
  {path:'', component:MainPageComponent},
  {path:'regression', component:RegChartComponent},
  {path: 'dnn', component: RegDnnComponent},
  {path: 'polynomial-regression', component: PolynRegComponent},
  {path: 'logistic-regression', component: LogRegComponent},
  {path: 'simple-moving-averages', component: MovAvgComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
