import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.

    // lazy-loading 방식
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 전역변수 실습 코드
// // router 객체를 사용해야 하기 때문에 const router 이후에 작성해주어야 함!
// router.beforeEach((to, from, next) => {

//   // 로그인 여부 변수 생성
//   const isLoggedIn = false

//   // 로그인이 필요한 페이지를 변수에 저장해주기(라우터에 등록한 name)
//   // const authPages = ['hello', 'home', 'about']
//   // 로그인 안해도 접속가능한 페이지를 설정해줘도 됨!
//   const allowAllPages = ['login']

//   // 이동해야 할 페이지(to)가 로그인이 필요한 사이트인지 확인하기
//   const isAuthRequired = authPages.includes(to.name)
  
//   // to가 로그인이 필요한 페이지이고, 현재 로그인이 되어 있지 않으면 Login페이지로 이동
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동!')
//     next({ name: 'login'})
//   // 그렇지 않으면 기존루트로 이동
//   } else {
//     console.log('to로 이동!')
//     next()
//   }
// })

export default router
