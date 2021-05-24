<template>
  <!--  size = 18-->
  <v-container>
    <v-card-title class="headline">
      Área do aluno
    </v-card-title>
    <v-btn
      color="primary"
      nuxt
      to="/avaliacao"
    >
      + adicione sua avaliação
    </v-btn>
    <v-row dense align="stretch">
      <!--      1ºbloco-->
      <v-col cols="4">
        <v-card>
          <v-card-text class="primary--text">
            <v-btn
              color="primary"
              text
              @click="reserve"
            >
              CES 111 - PROFESSORA MARINA
            </v-btn>
            <v-rating
              align = "center"
              :value="4.5"
              color="primary"
              dense
              half-increments
              readonly
              size="18"
            ></v-rating>
            <div align = "center"  class="grey--text ms-4">4.5</div>

            <v-btn
              color="primary"
              text
              @click="reserve"
            >
              CES 000 - PROFESSORA MARINA
            </v-btn>
            <v-rating
              align = "center"
              :value="3.5"
              color="primary"
              dense
              half-increments
              readonly
              size="18"
            ></v-rating>
            <div align = "center"  class="grey--text ms-4">4.5</div>

            <v-btn
              color="primary"
              text
              @click="reserve"
            >
              CES 555 - PROFESSORA MARINA
            </v-btn>
            <v-rating
              align = "center"
              :value="2.0"
              color="primary"
              dense
              half-increments
              readonly
              size="18"
            ></v-rating>
            <div align = "center"  class="grey--text ms-4">4.5</div>
          </v-card-text>
        </v-card>
      </v-col>
      </v-card-text>
      </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
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
      variavel: 14
    }
  },
}
</script>

<style scoped>

</style>
