import json
import os
import random
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

KV = r'''
#:import dp kivy.metrics.dp

<CardBox@BoxLayout>:
    orientation: 'vertical'
    padding: dp(14)
    spacing: dp(8)
    size_hint_y: None
    height: self.minimum_height
    canvas.before:
        Color:
            rgba: 0.09, 0.12, 0.20, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [22, 22, 22, 22]

<NavButton@Button>:
    background_normal: ''
    background_down: ''
    background_color: (0, 0, 0, 0)
    color: 1, 1, 1, 1
    bold: True
    font_size: '14sp'
    canvas.before:
        Color:
            rgba: 0.16, 0.63, 0.59, 1 if self.state == 'normal' else 0.13, 0.53, 0.49, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [18, 18, 18, 18]

<ActionButton@Button>:
    background_normal: ''
    background_down: ''
    background_color: (0, 0, 0, 0)
    color: 1, 1, 1, 1
    bold: True
    font_size: '15sp'
    size_hint_y: None
    height: dp(48)
    canvas.before:
        Color:
            rgba: 0.20, 0.38, 0.90, 1 if self.state == 'normal' else 0.15, 0.30, 0.75, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [18, 18, 18, 18]

<SoftInput@TextInput>:
    size_hint_y: None
    height: dp(46)
    multiline: False
    padding: [dp(12), dp(12), dp(12), dp(12)]
    background_normal: ''
    background_active: ''
    background_color: 0.16, 0.19, 0.29, 1
    foreground_color: 1, 1, 1, 1
    cursor_color: 1, 1, 1, 1
    hint_text_color: 0.75, 0.78, 0.85, 1

<MultiInput@TextInput>:
    size_hint_y: None
    height: dp(120)
    multiline: True
    padding: [dp(12), dp(12), dp(12), dp(12)]
    background_normal: ''
    background_active: ''
    background_color: 0.16, 0.19, 0.29, 1
    foreground_color: 1, 1, 1, 1
    cursor_color: 1, 1, 1, 1
    hint_text_color: 0.75, 0.78, 0.85, 1

<SoftSpinner@Spinner>:
    size_hint_y: None
    height: dp(46)
    background_normal: ''
    background_color: 0.16, 0.19, 0.29, 1
    color: 1, 1, 1, 1

<MetricTile@BoxLayout>:
    title: ''
    value: ''
    orientation: 'vertical'
    padding: dp(12)
    spacing: dp(4)
    size_hint_y: None
    height: dp(92)
    canvas.before:
        Color:
            rgba: 0.13, 0.17, 0.28, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20, 20, 20, 20]
    Label:
        text: root.title
        size_hint_y: None
        height: dp(22)
        color: .75, .82, .98, 1
        text_size: self.width, None
        halign: 'left'
        valign: 'middle'
        font_size: '13sp'
    Label:
        text: root.value
        color: 1, 1, 1, 1
        text_size: self.width, None
        halign: 'left'
        valign: 'middle'
        bold: True
        font_size: '24sp'

<SectionTitle@Label>:
    color: 1, 1, 1, 1
    size_hint_y: None
    height: dp(28)
    font_size: '18sp'
    bold: True
    text_size: self.width, None
    halign: 'left'
    valign: 'middle'

<MainRoot>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(10)
    canvas.before:
        Color:
            rgba: 0.05, 0.07, 0.12, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        size_hint_y: None
        height: dp(78)
        padding: dp(14)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: 0.08, 0.10, 0.18, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [26, 26, 26, 26]
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'EcoVision FAETEC'
                color: 1, 1, 1, 1
                bold: True
                text_size: self.width, None
                halign: 'left'
                valign: 'middle'
                font_size: '22sp'
            Label:
                text: 'Inovação, impacto e apresentação em um único app'
                color: .76, .82, .95, 1
                text_size: self.width, None
                halign: 'left'
                valign: 'middle'
                font_size: '12sp'
        Label:
            text: 'FAETEC'
            size_hint_x: None
            width: dp(76)
            bold: True
            color: 0.10, 0.12, 0.18, 1
            canvas.before:
                Color:
                    rgba: 0.39, 0.94, 0.80, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20, 20, 20, 20]

    BoxLayout:
        size_hint_y: None
        height: dp(52)
        spacing: dp(8)
        NavButton:
            text: 'Painel'
            on_release: app.switch_screen('dashboard')
        NavButton:
            text: 'Ideias'
            on_release: app.switch_screen('ideas')
        NavButton:
            text: 'Impacto'
            on_release: app.switch_screen('impact')
        NavButton:
            text: 'Pitch'
            on_release: app.switch_screen('pitch')
        NavButton:
            text: 'Salvos'
            on_release: app.switch_screen('saved')

    ScreenManager:
        id: screen_manager

        Screen:
            name: 'dashboard'
            ScrollView:
                do_scroll_x: False
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(4)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height

                    CardBox:
                        SectionTitle:
                            text: 'Visão geral do projeto'
                        Label:
                            text: 'Transforme uma boa ideia em uma apresentação forte. Gere propostas, calcule impacto e monte seu pitch.'
                            color: .82, .87, .97, 1
                            text_size: self.width, None
                            halign: 'left'
                            valign: 'top'
                            size_hint_y: None
                            height: self.texture_size[1]
                        BoxLayout:
                            size_hint_y: None
                            height: dp(196)
                            spacing: dp(8)
                            orientation: 'vertical'
                            MetricTile:
                                id: score_label
                                title: 'Score de inovação'
                                value: '0'
                            MetricTile:
                                id: streak_label
                                title: 'Ações registradas'
                                value: '0'
                        BoxLayout:
                            size_hint_y: None
                            height: dp(196)
                            spacing: dp(8)
                            orientation: 'vertical'
                            MetricTile:
                                id: idea_count_label
                                title: 'Ideias salvas'
                                value: '0'
                            MetricTile:
                                id: pitch_count_label
                                title: 'Pitchs criados'
                                value: '0'

                    CardBox:
                        SectionTitle:
                            text: 'Radar do app'
                        BoxLayout:
                            id: feed_box
                            orientation: 'vertical'
                            spacing: dp(8)
                            size_hint_y: None
                            height: self.minimum_height

        Screen:
            name: 'ideas'
            ScrollView:
                do_scroll_x: False
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(4)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    CardBox:
                        SectionTitle:
                            text: 'Laboratório de ideias'
                        Label:
                            text: 'Misture problema real + tecnologia + impacto social para gerar uma proposta forte.'
                            color: .82, .87, .97, 1
                            text_size: self.width, None
                            halign: 'left'
                            valign: 'top'
                            size_hint_y: None
                            height: self.texture_size[1]
                        SoftSpinner:
                            id: category_spinner
                            text: 'Escolha a área'
                            values: ['Energia', 'Água', 'Resíduos', 'Acessibilidade', 'Segurança', 'Educação']
                        SoftSpinner:
                            id: scope_spinner
                            text: 'Escolha o alcance'
                            values: ['Sala', 'Escola inteira', 'Comunidade', 'Bairro']
                        SoftSpinner:
                            id: audience_spinner
                            text: 'Escolha o público'
                            values: ['Alunos', 'Professores', 'Funcionários', 'Moradores', 'Todos']
                        ActionButton:
                            text: 'Gerar ideia impressionante'
                            on_release: app.generate_idea()
                        Label:
                            id: idea_output
                            text: 'Sua ideia vai aparecer aqui.'
                            color: 1, 1, 1, 1
                            text_size: self.width, None
                            halign: 'left'
                            valign: 'top'
                            size_hint_y: None
                            height: max(self.texture_size[1], dp(90))
                        ActionButton:
                            text: 'Salvar ideia'
                            on_release: app.save_current_idea()

        Screen:
            name: 'impact'
            ScrollView:
                do_scroll_x: False
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(4)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    CardBox:
                        SectionTitle:
                            text: 'Simulador de impacto'
                        Label:
                            text: 'Digite valores simples e gere números fortes para usar na apresentação.'
                            color: .82, .87, .97, 1
                            text_size: self.width, None
                            halign: 'left'
                            valign: 'top'
                            size_hint_y: None
                            height: self.texture_size[1]
                        SoftInput:
                            id: led_input
                            hint_text: 'Quantidade de lâmpadas LED instaladas'
                            input_filter: 'int'
                        SoftInput:
                            id: water_input
                            hint_text: 'Litros de água reaproveitados por mês'
                            input_filter: 'int'
                        SoftInput:
                            id: recycle_input
                            hint_text: 'Kg de recicláveis recolhidos por mês'
                            input_filter: 'int'
                        SoftInput:
                            id: students_input
                            hint_text: 'Pessoas impactadas'
                            input_filter: 'int'
                        ActionButton:
                            text: 'Calcular impacto'
                            on_release: app.calculate_impact()
                        Label:
                            id: impact_output
                            text: 'Os resultados do impacto aparecerão aqui.'
                            color: 1, 1, 1, 1
                            text_size: self.width, None
                            halign: 'left'
                            valign: 'top'
                            size_hint_y: None
                            height: max(self.texture_size[1], dp(110))

        Screen:
            name: 'pitch'
            ScrollView:
                do_scroll_x: False
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(4)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    CardBox:
                        SectionTitle:
                            text: 'Gerador de pitch'
                        SoftInput:
                            id: team_input
                            hint_text: 'Equipe ou turma'
                        SoftInput:
                            id: project_input
                            hint_text: 'Nome do projeto'
                        SoftInput:
                            id: target_input
                            hint_text: 'Quem será beneficiado?'
                        MultiInput:
                            id: problem_input
                            hint_text: 'Qual problema você quer resolver?'
                        MultiInput:
                            id: solution_input
                            hint_text: 'Descreva a solução em poucas linhas'
                        ActionButton:
                            text: 'Montar pitch vencedor'
                            on_release: app.generate_pitch()
                        Label:
                            id: pitch_output
                            text: 'Seu pitch vai aparecer aqui.'
                            color: 1, 1, 1, 1
                            text_size: self.width, None
                            halign: 'left'
                            valign: 'top'
                            size_hint_y: None
                            height: max(self.texture_size[1], dp(160))
                        ActionButton:
                            text: 'Salvar pitch'
                            on_release: app.save_current_pitch()

        Screen:
            name: 'saved'
            ScrollView:
                do_scroll_x: False
                BoxLayout:
                    id: saved_box
                    orientation: 'vertical'
                    padding: dp(4)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
'''


class MainRoot(BoxLayout):
    pass


class MetricTile(BoxLayout):
    title = StringProperty('')
    value = StringProperty('0')


class SectionTitle(Label):
    pass


class EcoVisionApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_file = 'ecovision_data.json'
        self.data = self.load_data()
        self.current_idea = ''
        self.current_pitch = ''

    def build(self):
        self.title = 'EcoVision FAETEC'
        Builder.load_string(KV)
        root = MainRoot()
        self.root = root
        self.refresh_all()
        return root

    def load_data(self):
        base = {
            'ideas': [],
            'pitches': [],
            'simulations': [],
            'actions': 0,
            'created_at': datetime.now().isoformat(timespec='seconds')
        }
        if not os.path.exists(self.data_file):
            return base
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
            base.update(loaded)
            return base
        except Exception:
            return base

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
        if screen_name == 'saved':
            self.refresh_saved()

    def touch_action(self):
        self.data['actions'] = int(self.data.get('actions', 0)) + 1
        self.save_data()
        self.refresh_dashboard()

    def refresh_all(self):
        self.refresh_dashboard()
        self.refresh_saved()

    def refresh_dashboard(self):
        ideas = len(self.data.get('ideas', []))
        pitches = len(self.data.get('pitches', []))
        simulations = len(self.data.get('simulations', []))
        actions = int(self.data.get('actions', 0))
        innovation_score = ideas * 12 + pitches * 14 + simulations * 10 + min(actions * 2, 50)

        self.root.ids.score_label.value = str(innovation_score)
        self.root.ids.streak_label.value = str(actions)
        self.root.ids.idea_count_label.value = str(ideas)
        self.root.ids.pitch_count_label.value = str(pitches)

        feed = self.root.ids.feed_box
        feed.clear_widgets()
        insights = [
            f'Você já registrou {ideas} ideia(s). Quanto mais ideias salvas, mais forte fica a defesa do projeto.',
            f'O app já montou {pitches} pitch(s). Use isso para ensaiar uma fala curta e impactante.',
            f'Foram feitas {simulations} simulação(ões) de impacto. Números concretos convencem muito mais.',
            'Projetos com problema real + tecnologia simples + benefício social costumam chamar muita atenção.',
            'Uma boa apresentação melhora quando você mostra economia, impacto ambiental e facilidade de implantação.'
        ]
        for text in insights[:4]:
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(88), padding=dp(12))
            with card.canvas.before:
                from kivy.graphics import Color, RoundedRectangle
                Color(0.13, 0.17, 0.28, 1)
                card._rect = RoundedRectangle(pos=card.pos, size=card.size, radius=[18, 18, 18, 18])
            def _update_rect(instance, _value):
                instance._rect.pos = instance.pos
                instance._rect.size = instance.size
            card.bind(pos=_update_rect, size=_update_rect)
            label = Label(
                text=text,
                color=(1, 1, 1, 1),
                text_size=(0, None),
                halign='left',
                valign='middle'
            )
            label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
            card.add_widget(label)
            feed.add_widget(card)

    def popup(self, title, text):
        content = BoxLayout(orientation='vertical', padding=dp(14), spacing=dp(10))
        message = Label(text=text, color=(1, 1, 1, 1))
        message.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
        btn = Button(text='OK', size_hint_y=None, height=dp(44), background_normal='', background_color=(0.20, 0.38, 0.90, 1))
        content.add_widget(message)
        content.add_widget(btn)
        popup = Popup(title=title, content=content, size_hint=(0.86, 0.42), separator_color=(0.39, 0.94, 0.80, 1), background='')
        btn.bind(on_release=popup.dismiss)
        popup.open()

    def generate_idea(self):
        category = self.root.ids.category_spinner.text
        scope = self.root.ids.scope_spinner.text
        audience = self.root.ids.audience_spinner.text
        if 'Escolha' in category or 'Escolha' in scope or 'Escolha' in audience:
            self.popup('Faltam dados', 'Escolha área, alcance e público antes de gerar a ideia.')
            return

        problem_bank = {
            'Energia': ['desperdício de energia em salas vazias', 'gastos altos com iluminação', 'falta de monitoramento do consumo'],
            'Água': ['desperdício em banheiros e pátios', 'falta de reaproveitamento da chuva', 'uso pouco eficiente da água'],
            'Resíduos': ['mistura de lixo reciclável e orgânico', 'falta de coleta inteligente', 'baixo engajamento na reciclagem'],
            'Acessibilidade': ['dificuldade de orientação e inclusão', 'barreiras de comunicação', 'falta de apoio visual e sonoro'],
            'Segurança': ['falta de alertas rápidos', 'baixa prevenção de riscos', 'comunicação lenta em incidentes'],
            'Educação': ['baixa participação em projetos', 'dificuldade de transformar teoria em prática', 'falta de dados para mostrar resultados']
        }
        tech_bank = {
            'Energia': ['sensores simples com painel de monitoramento', 'painel em tempo real com metas por turma', 'alertas automáticos de consumo fora do padrão'],
            'Água': ['medição inteligente com metas por bloco', 'mapa de uso com pontos de reaproveitamento', 'sistema de captação e monitoramento local'],
            'Resíduos': ['lixeiras inteligentes com pontuação por turma', 'painel visual de coleta seletiva', 'desafio gamificado com ranking sustentável'],
            'Acessibilidade': ['assistente visual e sonoro por QR Code', 'rotas acessíveis com orientação simplificada', 'painel inclusivo com leitura facilitada'],
            'Segurança': ['botão digital de alerta com histórico', 'painel de zonas de risco', 'protocolo inteligente de comunicação interna'],
            'Educação': ['plataforma de desafios reais com score', 'gerador de projetos com simulação de impacto', 'hub para apresentar resultados e evidências']
        }

        problem = random.choice(problem_bank[category])
        tech = random.choice(tech_bank[category])
        innovation = random.randint(82, 98)
        viability = random.randint(76, 95)
        impact = random.randint(80, 99)

        text = (
            f'Projeto sugerido: {category} Inteligente para {scope}\n\n'
            f'Problema atacado: {problem}.\n'
            f'Solução: criar uma proposta focada em {audience.lower()}, usando {tech}.\n\n'
            f'Diferencial: o sistema transforma dados reais em ações visíveis, facilitando gestão, engajamento e apresentação.\n'
            f'Inovação: {innovation}/100 | Viabilidade: {viability}/100 | Impacto: {impact}/100\n\n'
            f'Nome forte sugerido: Eco{category[:4].title()} Vision {scope.replace(" ", "")}'
        )
        self.current_idea = text
        self.root.ids.idea_output.text = text
        self.touch_action()

    def save_current_idea(self):
        if not self.current_idea.strip():
            self.popup('Nada para salvar', 'Gere uma ideia antes de salvar.')
            return
        self.data['ideas'].append({
            'text': self.current_idea,
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        })
        self.save_data()
        self.refresh_all()
        self.touch_action()
        self.popup('Ideia salva', 'Sua ideia foi salva no histórico do app.')

    def calculate_impact(self):
        def get_int(widget_id):
            value = self.root.ids[widget_id].text.strip()
            return int(value) if value else 0

        led = get_int('led_input')
        water = get_int('water_input')
        recycle = get_int('recycle_input')
        students = get_int('students_input')

        kwh_saved = led * 9
        water_saved = water
        co2_avoided = round((kwh_saved * 0.084) + (recycle * 1.8), 2)
        engagement = min(100, students * 2)
        score = (led * 2) + (water // 20) + (recycle * 4) + students

        text = (
            f'Resultado estimado do projeto\n\n'
            f'• Economia de energia: {kwh_saved} kWh/mês\n'
            f'• Água reaproveitada: {water_saved} litros/mês\n'
            f'• Recicláveis desviados do lixo comum: {recycle} kg/mês\n'
            f'• CO₂ evitado estimado: {co2_avoided} kg/mês\n'
            f'• Engajamento social previsto: {engagement}%\n'
            f'• Score geral do impacto: {score}\n\n'
            f'Frase para apresentação: “Nosso projeto converte pequenas ações em economia mensurável e impacto ambiental visível.”'
        )
        self.root.ids.impact_output.text = text
        self.data['simulations'].append({
            'led': led,
            'water': water,
            'recycle': recycle,
            'students': students,
            'result': text,
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        })
        self.save_data()
        self.refresh_all()
        self.touch_action()

    def generate_pitch(self):
        team = self.root.ids.team_input.text.strip() or 'Equipe FAETEC'
        project = self.root.ids.project_input.text.strip() or 'Projeto Inovador'
        target = self.root.ids.target_input.text.strip() or 'a comunidade escolar'
        problem = self.root.ids.problem_input.text.strip() or 'um problema real ainda pouco resolvido'
        solution = self.root.ids.solution_input.text.strip() or 'uma solução prática, tecnológica e fácil de aplicar'

        pitch = (
            f'Pitch de 30 segundos\n\n'
            f'“Nós somos a {team} e criamos o {project}. Percebemos que {problem} afeta diretamente {target}. '
            f'Por isso, desenvolvemos {solution}. Nossa proposta combina inovação, viabilidade e impacto social, '
            f'permitindo resultados claros, apresentação forte e possibilidade real de implantação. '
            f'Não é só uma ideia bonita: é uma solução útil, mensurável e pronta para crescer.”\n\n'
            f'Fechamento forte: “Queremos transformar necessidade em resultado e mostrar que tecnologia escolar também pode mudar realidades.”'
        )
        self.current_pitch = pitch
        self.root.ids.pitch_output.text = pitch
        self.touch_action()

    def save_current_pitch(self):
        if not self.current_pitch.strip():
            self.popup('Nada para salvar', 'Gere um pitch antes de salvar.')
            return
        self.data['pitches'].append({
            'text': self.current_pitch,
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        })
        self.save_data()
        self.refresh_all()
        self.touch_action()
        self.popup('Pitch salvo', 'Seu pitch foi salvo no histórico do app.')

    def refresh_saved(self):
        box = self.root.ids.saved_box
        box.clear_widgets()

        header = Label(
            text='Histórico do app',
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            bold=True,
            font_size='20sp'
        )
        box.add_widget(header)

        if not self.data['ideas'] and not self.data['pitches'] and not self.data['simulations']:
            empty = Label(
                text='Ainda não há itens salvos. Gere ideias, impactos e pitchs para preencher seu portfólio.',
                size_hint_y=None,
                height=dp(90),
                color=(0.9, 0.92, 0.98, 1)
            )
            box.add_widget(empty)
            return

        sections = [
            ('Ideias', self.data['ideas'][-3:][::-1]),
            ('Pitchs', self.data['pitches'][-3:][::-1]),
            ('Simulações', self.data['simulations'][-3:][::-1]),
        ]

        from kivy.graphics import Color, RoundedRectangle

        for title, items in sections:
            title_label = Label(
                text=title,
                size_hint_y=None,
                height=dp(34),
                color=(0.39, 0.94, 0.80, 1),
                bold=True,
                font_size='17sp',
                text_size=(0, None),
                halign='left',
                valign='middle'
            )
            title_label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
            box.add_widget(title_label)
            if not items:
                none_label = Label(
                    text='Sem registros nessa seção.',
                    size_hint_y=None,
                    height=dp(40),
                    color=(0.82, 0.87, 0.97, 1)
                )
                box.add_widget(none_label)
                continue
            for item in items:
                card = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(12), spacing=dp(6))
                text = item.get('text') or item.get('result', '')
                preview = text if len(text) <= 340 else text[:340] + '...'
                card.height = dp(150)
                with card.canvas.before:
                    Color(0.09, 0.12, 0.20, 1)
                    card._rect = RoundedRectangle(pos=card.pos, size=card.size, radius=[20, 20, 20, 20])
                def _update_rect(instance, _value):
                    instance._rect.pos = instance.pos
                    instance._rect.size = instance.size
                card.bind(pos=_update_rect, size=_update_rect)
                stamp = Label(text=item.get('created_at', ''), size_hint_y=None, height=dp(20), color=(0.39, 0.94, 0.80, 1), bold=True)
                stamp.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
                body = Label(text=preview, color=(1, 1, 1, 1), halign='left', valign='top')
                body.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
                card.add_widget(stamp)
                card.add_widget(body)
                box.add_widget(card)


if __name__ == '__main__':
    EcoVisionApp().run()
