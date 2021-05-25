<template>
  <v-card
    class="mx-auto"
    width="1500"
  >
    <v-list>
      <v-list-group
        :value="true"
        v-for="(disc, i) in disciplinas"
      >
        <template v-slot:activator>
          <v-list-item-title>{{ disc[0] }}</v-list-item-title>
        </template>
        <v-list-item
          v-for="(x, j) in disc[1]"
          :key="j"
        >
          <v-list-item-title v-text="x"></v-list-item-title>
          <v-btn
            color="primary"
            dark
            @click.stop="dialog = true"
          >Abrir Dialog
          </v-btn>
          <v-dialog
            class="mx-auto"
            width="1000"
            v-model="dialog">
            <v-card>
              <v-card-title>
                {{disc[0]}} - {{x}}
              </v-card-title>
              <v-card-text>
                Tchau
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script>

export default {
  name: "comp",
  data: () => ({
    dialog: false,
    disciplinas: [
      ['CES-22', ['Karla']],
      ['CES-11', ['Armando', 'Curtis']],
      ['CES-12', ['Alonso']],
    ],
  }),
}
</script>

<style scoped>

</style>
