import { Routes,CanActivate } from '@angular/router';
import { AppComponent } from './app.component';
import { FrontComponent } from './front/front.component';
import { BackComponent } from './back/back.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';

const route: Routes = [

    {
        path:'',
        component:FrontComponent
    },
    {
        path:'front',
        component:FrontComponent
    },
    {
        path:'back',
        component:BackComponent
    },
    {
        path:'**',
        component:PagenotfoundComponent
    }
    
    
  
];
export default route;