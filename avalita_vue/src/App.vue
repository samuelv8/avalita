<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link id="oi" to="/" class="navbar-item">
          <img src="https://i.imgur.com/HrV8xwb.png" alt="logotipo do avalita"
          />
        </router-link>

        <a
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbar-menu"
            @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>

          <span aria-hidden="true"></span>

          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
          class="navbar-menu"
          id="navbar-menu"
          v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link
              v-for="dpto in departamentos"
              :key="dpto.id"
              :to="dpto.get_absolute_url"
              class="navbar-item"
          >{{
              get_slug_from_url(dpto.get_absolute_url).toUpperCase()
            }}
          </router-link
          >

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/area_aluno" class="button is-success">
                  <span class="icon"
                  ><i class="fas fa-graduation-cap"></i
                  ></span>

                  <span>Área do Aluno</span>
                </router-link>

                <div>
                  <button @click="sair()" class="button is-danger">Sair</button>
                </div>
              </template>

              <template v-else>
                <router-link to="/cadastro" class="button is-light"
                >Cadastre-se
                </router-link
                >
                <router-link to="/login" class="button is-light"
                >Login
                </router-link
                >
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div
        class="is-loading-bar has-text-centered"
        v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Avalita | Copyright &copy; 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showMobileMenu: false,
      departamentos: [],
      h: 42,
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.getAllDepartamentos();
  },
  methods: {
    async getAllDepartamentos() {
      this.$store.commit("setIsLoading", true);
      await axios
          .get("/api/v1/all-departamentos/")
          .then((response) => {
            this.departamentos = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      this.$store.commit("setIsLoading", false);
    },
    get_slug_from_url(url) {
      return url.substring(6, url.length - 1);
    },
    sair() {
      axios.post("/api/v1/auth/token/logout/")
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>