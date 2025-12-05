import logging
import re
from functools import cache
from typing import TYPE_CHECKING, Union

from transformers import AutoTokenizer


if TYPE_CHECKING:
    import transformers


eval_logger = logging.getLogger(__name__)

DEFAULT_SEQ_LENGTHS = [
    4096,
]

SUBSTANTIVOS = [
    "Filipe","Tiago","Rodrigo","Clara","Silva","Ferreira","Brasil","Rio de Janeiro","Macapá","Jericoacoara",
    "Equador","Tailândia","Lisboa","Portugal","Bidu","Bolinha","Fifi","Rex","Amazonas","Solimões","Negro",
    "Tietê","Nilo","Mississipi","Danúbio","Atlântico","Pacífico","Mediterrâneo","Egeu","Everest","Andes",
    "Himalaias","Pirinéus","Sol","Lua","Terra","Marte","Saturno","Carnaval","Natal","Páscoa","Ano Novo",
    "Saci","Iara","Curupira","Zeus","Afrodite","Aquiles","Nike","Avon","Colgate","Pepsi","Nintendo",
    "Grande Sertão: Veredas","O Sítio do Pica-pau Amarelo","O Globo","O Estado de São Paulo",
    "Organização das Nações Unidas","Universidade Federal do Rio de Janeiro","Ministério da Educação",

    "livro","caneta","garfo","panela","mesa","cama","microfone","celular","martelo","bolsa","criança",
    "menina","garoto","pai","mãe","homem","mulher","professor","médica","estudante","ator","empresário",
    "cachorro","gato","cavalo","tigre","papagaio","mico","capivara","palmeira","roseira","samambaia",
    "capim","coqueiro","girassol","goiaba","banana","pitanga","laranja","limão","mamão","montanha","ilha",
    "lago","rio","mangue","serra","bairro","cidade","país","manhã","noite","dia","sol","chuva","vento",
    "mês","século","fada","fantasma","bruxa","sereia","vampiro",

    "flor","roupa","água","canela","planeta","recado","vida","papelaria","drogaria","espera","força",
    "carinho","amizade","diversão","povo","colega","jardineiro","telefonista","marreco","águia","boto",
    "peixinho","manga","ovo","passeio","fome","calor","frio","casinha","cartão",

    "álbum","alcateia","armada","arquipélago","arvoredo","bando","bateria","boiada","cacho","cáfila",
    "caravana","cardume","coletânea","colmeia","colônia","comitiva","constelação","cordilheira","enxame",
    "esquadrilha","fardo","feixe","fornada","frota","junta","júri","manada","matilha","ninhada","nuvem",
    "orquestra","panapaná","penca","pilha","plateia","pomar","praga","ramalhete","rebanho","renque",
    "resma","réstia","saraivada","time","tripulação","tropa","turma","vara",

    "arco-íris","quebra-cabeça","segunda-feira","decreto-lei","matéria-prima","cachorro-quente",
    "cavalo-marinho","primeiro-ministro","guarda-chuva","porta-chaves","peixe-espada","bate-papo",
    "beija-flor","corre-corre","couve-flor","tique-taque","turma-piloto","roda-viva","paraquedas",
    "passatempo","pontapé","vaivém","planalto","vinagre","girassol","malmequer","mandachuva",
    "madrepérola","destarte","cor-de-rosa","cana-de-açúcar","bem-me-quer","bem-te-vi",

    "cadeira","cortina","rádio","pente","caderno","borracha","janela","tijolo","telha","relógio",
    "garrafa","jacaré","golfinho","serpente","rinoceronte","hipopótamo","formiga","galinha","jaca",
    "pitanga","laranja","melancia","maçã","maracujá","caqui","samambaia","capim","ipê","margarida",
    "cacto","chuva","vento","trovoada","neve","noite","homem","mulher","professora","dentista",
    "porteiro","psicóloga","advogado","praia","jardim","feira","cinema","bruxa","duende","unicórnio",
    "lobisomem","vampiro",

    "alegria","tristeza","saudade","orgulho","inveja","vergonha","ira","amor","humildade","seriedade",
    "compreensão","confusão","esperança","frieza","amizade","bondade","educação","honestidade",
    "facilidade","complexidade","cor","tamanho","peso","altura","comprimento","espessura","doença",
    "saúde","infância","velhice","pobreza","riqueza","bem-estar","fome","sede","calor","recuperação",
    "organização","desenvolvimento","crescimento","arrumação","elaboração","ensino","aprendizagem",
    "responsabilidade",

    "terra","mar","poeira","pedra","corpo","livro","boca","papel","luz","flor","chuva","casa","porta",
    "sapato","açúcar","cachorro","jornal","ano","árvore","coisa","ferro","fogo","folha","homem","tempo",
    "quilo","jardim","equilíbrio","avião","café","tucano","algodão","laranja",

    "território","terraço","marítimo","marinho","empoeirado","desempoeirar","pedreiro","apedrejar",
    "corpanzil","corporal","livreiro","livrete","desbocado","bucal","papeleiro","papelão","luzir",
    "reluzente","florido","floreado","chuvada","chuvisco","casario","caseiro","portão","portal",
    "sapateado","sapateiro","açucareiro","açucarado","equilibrado","desequilibrar","anual","anuário",
    "temporário","temporão","jardinagem","jardineiro","laranjada","laranjal","cachorrada","cachorrice",
    "jornalista","jornaleiro","folhagem","desfolhar","ferreiro","ferrador","arvoredo","arvorar",
    "fogoso","foguear","homenzarrão","cachorrinho",

    "jovem","colega","cliente","chefe","fã","estudante","gerente","agente","doente","camarada","artista",
    "policial","indígena","dentista","pianista","jornalista","intérprete","imigrante","colegial",
    "anarquista","compatriota","selvagem","servente","herege","jurista","mártir","taxista",

    "pessoa","ser","criança","indivíduo","testemunha","vítima","criatura","anjo","gênio","ídolo",
    "monstro","neném","cônjuge","estrela de cinema","ente","apóstolo","carrasco","defunto",

    "cobra","águia","cavalo-marinho","chimpanzé","escorpião","dromedário","hipopótamo","tartaruga",
    "formiga","crocodilo","pinguim","pulga","gaivota","baleia","barata","girafa","gorila","serpente",
    "mosca","mosquito","zebra","onça","tigre","borboleta","camaleão","capivara","beija-flor","aranha",
    "boto","jiboia","jacaré","foca","besouro","sapo","tatu","panda","sardinha","peixe","polvo",
    "rinoceronte","hiena","rouxinol","andorinha","abutre","gavião","corvo","falcão","condor"
]

ADJETIVOS = [
    "bom","mau","grande","pequeno","novo","velho","alto","baixo","feliz","triste",
    "bonito","feio","forte","fraco","rápido","lento","fácil","difícil","calmo","nervoso",
    "quente","frio","cheio","vazio","caro","barato","doce","amargo","salgado","amigo",
    "inimigo","inteligente","burro","honesto","mentiroso","limpo","sujo","simples","complicado",
    "leve","pesado","famoso","desconhecido","rico","pobre","gordo","magro","justo","injusto",
    "perigoso","seguro","ruim","excelente","útil","inútil","curto","longo","rude","educado",
    "alegre","sério","engraçado","moderno","antigo","humilde","arrogante","prático","imprático",
    "vivo","morto","sadio","doente","liso","áspero","úmido","seco","forte","frágil",
    "curioso","indiferente","novo","velho","fresco","podre","normal","estranho","perfeito","imperfeito",
    "racional","irracional","necessário","desnecessário","sábio","ignorante","verdadeiro","falso",
    "generoso","egoísta","fiel","infiel"
]

VERBOS = [
    "amar","ir","fazer","estar","ser","ter","ver","vir","poder","dar","haver","pôr",
    "comer","querer","partir","falar","trazer","estudar","cantar","dizer","sair","ler",
    "saber","rir","correr","dormir","vender","beber","pedir","escrever","andar","sorrir",
    "ouvir","sentir","ficar","chegar","agir","gostar","brincar","abrir","caber","viver",
    "conseguir","comprar","jogar","cair","perder","manter","corrigir","passar","receber",
    "viajar","pensar","conhecer","assistir","aprender","dançar","começar","intervir",
    "seguir","trabalhar","crer","encontrar","precisar","deixar","dividir","levar","dever",
    "colorir","voltar","chamar","voar","subir","pular","entender","passear","fugir","expor",
    "nascer","compor","olhar","parar","achar","valer","usar","lembrar","medir","dirigir",
    "reaver","esquecer","morar","acordar","colocar","propor","proteger","ganhar","feder",
    "tomar","requerer","esperar",

    "pegar","descer","morrer","entrar","fingir","tossir","mexer","contar","possuir","ajudar",
    "bater","conversar","cumprir","mandar","chover","chorar","preferir","descobrir","continuar",
    "suar","lavar","doer","doar","acabar","desejar","vestir","imprimir","existir","decidir",
    "sonhar","prever","conter","sumir","caminhar","pagar","dispor","falir","procurar","nadar",
    "construir","divertir","prover","atender","acontecer","mudar","escolher","entreter","responder",
    "aderir","mentir","crescer","perdoar","fechar","almoçar","enviar","desistir","encher","tornar",
    "participar","parecer","realizar","servir","vencer","ligar","permitir","avisar","terminar",
    "sentar","demolir","tirar","buscar","polir","apresentar","sofrer","entregar","criar","casar",
    "levantar","perceber","impor","ferir","adquirir","rever","perguntar","repor","agradecer",
    "adequar","convidar","aceitar","precaver","tentar","mostrar","deter","ensinar","odiar",
    "acreditar","informar","visitar","pentear",

    "matar","aparecer","obter","aproveitar","beijar","respeitar","resolver","tocar","gritar","supor",
    "incluir","roer","zoar","surgir","compreender","cobrir","cuidar","pintar","julgar","excluir",
    "discutir","destruir","permanecer","escutar","ceder","oferecer","preparar","limpar","repetir",
    "imaginar","convir","competir","cortar","marcar","analisar","salvar","interagir","adorar","prender",
    "reter","reunir","roubar","preocupar","arrumar","varrer","plantar","garantir","virar","colher",
    "merecer","observar","abraçar","unir","ingerir","lutar","curtir","refletir","compartilhar","provir",
    "iniciar","abolir","sugerir","opor","diminuir","atingir","exigir","bloquear","acompanhar","soar",
    "maquiar","guardar","encaminhar","cozinhar","caçar","despedir","explicar","concluir","atrair",
    "contribuir","apoiar","magoar","aguardar","contradizer","defender","presentear","repartir","ansiar",
    "ocorrer","cansar","distrair","alcançar","lançar","produzir","exercer","insistir","satisfazer",
    "copiar","utilizar","considerar","transformar"
]

@cache
def get_tokenizer(
    tokenizer=None, pretrained=None, **kwargs
) -> Union["transformers.PreTrainedTokenizer", "transformers.PreTrainedTokenizerFast"]:
    pretrained = tokenizer or pretrained
    assert pretrained, "No tokenizer or pretrained provided."
    eval_logger.info(f"Using tokenizer {pretrained} for synthetic tasks.")
    return AutoTokenizer.from_pretrained(pretrained, trust_remote_code=True)


def postprocess_pred(prediction: list[str]) -> list[str]:
    res = []
    for predict_str in prediction:
        predict_str = predict_str.strip()

        # Remove all non-printable characters
        np_pattern = re.compile(r"[\x00-\x1f]")
        predict_str = np_pattern.sub("\n", predict_str).strip()
        res.append(predict_str)

    return res


def string_match_all(preds: list[str], refs: list[list[str]]) -> float:
    score = sum(
        [
            sum([1.0 if r.lower() in pred.lower() else 0.0 for r in ref]) / len(ref)
            for pred, ref in zip(preds, refs)
        ]
    ) / len(preds)
    return score


def string_match_part(preds: list[str], refs: list[list[str]]) -> float:
    score = max(
        [
            sum([1.0 if r.lower() in pred.lower() else 0.0 for r in ref]) / len(ref)
            for pred, ref in zip(preds, refs)
        ]
    ) / len(preds)
    return score


def process_results(doc: dict, results: list[str]) -> dict[str, float]:
    # hacky: set all other lengths to -1
    metrics = {str(length): -1.0 for length in DEFAULT_SEQ_LENGTHS}
    input_len = doc["max_length"]
    pred = postprocess_pred(results)
    score = string_match_all(pred, [doc["outputs"]])
    metrics[str(input_len)] = score
    return metrics


def process_results_part(doc: dict, results: list[str]) -> dict[str, float]:
    # hacky: set all other lengths to -1
    metrics = {str(length): -1.0 for length in DEFAULT_SEQ_LENGTHS}
    input_len = doc["max_length"]
    pred = postprocess_pred(results)
    score = string_match_part(pred, [doc["outputs"]])
    metrics[str(input_len)] = score
    return metrics


def aggregate_metrics(metrics: list[float]) -> float:
    res = [x for x in metrics if x != -1]
    if not res:
        # we don't have any samples with this length
        return -1
    return sum(res) / len(res)
