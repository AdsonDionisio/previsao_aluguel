const { createApp } = Vue;

createApp({

    data() {

        return {

             dados: {
                bairro: "Moema",
                tipo_imovel: "Apartamento",
                area_util: 80,
                banheiros: 2,
                suites: 1,
                quartos: 2,
                vagas_garagem: 1,
                taxa_condominio: 650,
                iptu_ano: 1800
            },

            resultado: null

        };

    },

    methods: {

        async prever() {
            try{
                const response = await axios.post(
                    '/prever_alugel/',
                     this.dados
                    );            
                this.resultado = response.data;
                //alert(`O valor do aluguel previsto é: R$ ${response.data.rental_value.toFixed(2)}`);    
            }catch (erro) {
                console.error(erro);

                if(erro.response)
                    alert(JSON.stringify(erro.response.data));
                else
                    alert(erro.message);
                 this.resultado = 0;
            }
        }
    }
}).mount('#app');