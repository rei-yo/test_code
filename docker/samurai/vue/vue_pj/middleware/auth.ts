export default defineNuxtRouteMiddleware((to, from) => {
    console.log('from', from);
    console.log('to', to);

    if (from.fullPath == '/'){
        return navigateTo('/');
    }
  });