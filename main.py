from kivy.app import App from kivy.uix.button import Button from kivy.uix.label import Label from kivy.uix.boxlayout import BoxLayout from kivy.core.window import Window

import alignment_script

class AlignmentApp(App): def build(self): Window.clearcolor = (1, 1, 1, 1)  # White background layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

self.status = Label(text="📋 Tap the button to generate alignment report",
                        color=(0, 0, 0, 1),
                        font_size='18sp')

    run_button = Button(text="▶️ Run Alignment Report",
                        size_hint=(1, 0.3),
                        background_color=(0.2, 0.6, 0.2, 1),
                        font_size='20sp')
    run_button.bind(on_press=self.run_report)

    layout.add_widget(self.status)
    layout.add_widget(run_button)
    return layout

def run_report(self, instance):
    try:
        alignment_script.main()
        self.status.text = "✅ Report generated successfully!"
    except Exception as e:
        self.status.text = f"❌ Error: {str(e)}"

if name == 'main': AlignmentApp().run()

