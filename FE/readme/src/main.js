import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

Vue.config.productionTip = false;

new Vue({
  router,
<<<<<<< HEAD
  vuetify,
=======
>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
  render: (h) => h(App)
}).$mount("#app");
