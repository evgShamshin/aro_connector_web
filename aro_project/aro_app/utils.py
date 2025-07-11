from aro_app.models import About, Tag, Group


class DataMixin:
    title = None
    descr = None
    about = None
    commands = None
    tags = None
    groups = None

    extra_context = {}

    def __init__(self):
        if self.title not in self.extra_context:
            self.extra_context['title'] = 'ARO Group'

        if self.descr == "Плагин Connector":
            self.extra_context['descr'] = """Плагин Connector - расширение для архитекторов и дизайнеров,
                         добавляющее возможности в Autodesk Revit.
                         Автоматизирует многие процессы и существенно сокращает время
                         создания модели.
                         Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                         версиями Autodesk Revit."""

        if self.descr == "BIM-консалтинг":
            self.extra_context['descr'] = """BIM-консалтинг - это комплекс услуг по внедрению,
                                        адаптации и оптимизации технологий информационного моделирования
                                        (BIM) на всех этапах жизненного цикла строительного проекта.
                                        Мы помогаем компаниям повысить эффективность работы,
                                        сократить сроки проектирования и минимизировать ошибки
                                        за счёт грамотного использования современных цифровых инструментов."""

        if self.commands:
            self.extra_context['commands'] = self.commands
