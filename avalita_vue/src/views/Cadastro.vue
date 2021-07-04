<template>
  <div class="page-cadastro">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Criar conta</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Login @ga</label>
            <div class="control">
              <input
                type="text"
                placeholder="nome.sobrenome"
                class="input"
                v-model="login_ga"
              />
            </div>
          </div>

          <div class="field">
            <label>Password (mínimo de 8 caracteres)</label>
            <div class="control">
              <input type="password" class="input" v-model="password" />
            </div>
          </div>

          <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input type="password" class="input" v-model="password2" />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">Sign up</button>
            </div>
          </div>

          <hr />

          Ou <router-link to="/login">clique aqui</router-link> para fazer
          login!
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "SignUp",
  data() {
    return {
      login_ga: "",
      password: "",
      password2: "",
      ano_entrada: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Criar Conta | Avalita";
  },
  methods: {
    submitForm() {
      this.errors = [];
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.login_ga,
          email: this.login_ga + "@ga.ita.br",
          password: this.password,
        };
        axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            toast({
              message: "Account created, please log in!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
            this.$router.push("/log-in");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>