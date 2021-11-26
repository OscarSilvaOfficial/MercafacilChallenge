<template>
    <v-navigation-drawer
      absolute
      permanent
      left
      class="menu"
    >
      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          @click="changePage(item.route)"
          class="menu--list zoom"
          link
        >
          <v-list-item-icon>
            <v-avatar>
              <img
                :src="item.image"
                alt="Icone"
                v-if="item.image.includes('/')"
              >
              <v-icon v-else class="menu__icon--image">
                {{ item.image }}
              </v-icon>
            </v-avatar>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="menu--title">{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { IMenu } from '@/intefaces/menu'

@Component
export default class Menu extends Vue {
  private items: IMenu[] = [
    { title: "Personagens", image: require("@/assets/img/menu-icon.jpg"), route:'characters' },
    { title: "Episódios", image: "mdi-account", route:'episodes' },
  ]

  changePage(name: string): void {
    if (this.$route.name !== name) this.$router.push({ name: name });
  }
}
</script>

<style lang="scss" scoped>
.v-list-item__icon {
  height: unset !important;
  margin-top: auto !important;
  margin-bottom: auto !important;
}

.menu {
  box-shadow: 5px 0px 5px black;
  background-color: rgb(24, 26, 27) !important;

  .zoom {
    transition: all .2s;
    
    &:hover {
      transform: scale(1.1) !important;
    }
  }

  &--list {
    height: 70px;
  }
  
  &__icon--image {
    color: #fff !important;
  }

  &--title {
    color: #fff !important;
    font-size: 14px !important;
  }
}
</style>