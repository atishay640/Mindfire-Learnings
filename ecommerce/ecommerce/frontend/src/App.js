import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import {
  Home,
  Blog,
  BlogDetail,
  Checkout,
  Contact,
  ShopDetails,
  ShopGrid,
  ShopingCart
} from './pages'


function App() {
  return (
    <div>
      <Router>
        <Switch>
          <Route exact path="/" >
            <Home/>
          </Route>
          <Route  exact path="/blog" >
            <Blog/>
          </Route>
          <Route  exact path="/blog/:id" >
            <BlogDetail/>
          </Route>
          <Route  exact path="/checkout" >
            <Checkout/>
          </Route>
          <Route  exact path="/contact" >
            <Contact/>
          </Route>
          <Route  exact path="/shop" >
            <ShopGrid/>
          </Route>
          <Route  exact path="/shop/:id" >
            <ShopDetails/>
          </Route>
          <Route  exact path="/cart" >
            <ShopingCart/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
