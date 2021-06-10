<template>
  <!--  size = 18-->
  <v-container fluid class="align-start">
    <v-row align="start" justify="start">
      <v-col
        align-self="start"
        md = "10"
        offset-md="1"
      >
        <v-card>
          <v-card-title class="headline">
            Área do aluno
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col
                order="first"
                sm="1"
              >
                <v-flex>
                  <v-avatar
                    color="primary"
                    size="56"
                  >
                    <span class="white--text text-h5">{{usr.firstLastNameInitials}}</span>
                  </v-avatar>
                </v-flex>
              </v-col>
              <v-col
                order="last"
                align-self="center"
              >
                <v-row>
                  <span class="black--text text-h4">{{usr.name}}</span>
                </v-row>
                <v-row>
                  <span class="black--text text-h5">{{usr.email}}</span>
                </v-row>
              </v-col>
            </v-row>
            <v-row align-content="center" justify="center">
              <v-col v-for="(semester, i) in usr.semesters" :key="i">
                <v-btn
                  color="cyan"
                  @click="show_avals=true"
                >{{semester}}</v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row align="start" justify="start">
      <v-col
        align-self="start"
        md="10"
        offset-md="1"
      >
        <v-card
          v-if="show_avals"
        >
          <v-card-actions>
            <v-btn
              color="primary"
              nuxt
              to="/avaliacao"
            >
              + Adicione sua avaliação
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              color="red"
              @click="show_avals=false"
            >
              Fechar
            </v-btn>
          </v-card-actions>
          <lista-avaliacoes/>
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import ListaAvaliacoes from "@/components/ListaAvaliacoes";

export default {
  name: "area-aluno",
  head() {
    const title = "Área do Aluno"
    return {
      title
    }
  },
  data() {
    return {
      show_avals: false,
      usr: {
        name: "Gabriel Barbosa Martinz",
        firstLastNameInitials: "GM",
        email: "example@ga.ita.br",
        semesters: ['2019.1', '2019.2', '2020.1', '2020.2', '2021.1', '2021.2', '2022.1', '2022.2', '2023.1', '2023.2'],
      }
    }
  },
  components: {
    ListaAvaliacoes,
  }
}
</script>

<style scoped>

</style>
