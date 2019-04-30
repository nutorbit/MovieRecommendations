import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Display from '@/views/Display.vue'
import store from '@/store'

Vue.use(Router)


let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/display',
      name: 'display',
      component: Display
    }
  ]
})

router.beforeEach((to, from, next) => {
    // console.log(store.getters.main)
    if(to.path == '/'){
      next()
    }
    else if(store.getters.getMain){
        next()
    }else{
        next({ path: "/" })
    }
})
export default router
