

export const authModule = {
    state: {
        current_user: {
            rec_book_num: null,
            username: null,
            surname: null,
            name: null,
            patronymic: null,
            e_mail: null,
            user_id: null,
            role_id: null,
        },
        isAuth: false
    },
    mutations: {
        setUser(state, current_user){
            state.current_user = current_user;
        },
        setAuth(state, isAuth){
            state.isAuth = isAuth;
        }
    },
    actions:{
        updateUser({commit}, current_user){
            console.log('Данные сохранены в локальный стор')
            commit('setUser', current_user)
            commit('setAuth', true)
        },
        logOutUser({commit}){
            console.log('Пользователь вышел ')
            commit('setUser', null)
            commit('setAuth', false)
        }

    },
    getters:{
        getUser(state){
            return state.current_user;
        },
        isAuth(state){
            return state.isAuth;
        }
    }
}