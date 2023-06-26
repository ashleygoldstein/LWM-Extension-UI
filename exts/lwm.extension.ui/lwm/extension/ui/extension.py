import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[lwm.extension.ui] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class LwmExtensionUiExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[lwm.extension.ui] lwm extension ui startup")

        self._count = 0

        self._window = ui.Window("Extension UI Example", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                with ui.HStack():
                    with ui.CollapsableFrame(title="Collapsable Frame"):
                        with ui.HStack():
                            ui.Label("Label Example", alignment=ui.Alignment.LEFT, style={"color": "red"})
                            ui.FloatSlider(min=0, max=50, style={"color": "pink", "font_size":20.0})

                    with ui.ScrollingFrame():
                        with ui.VStack():
                            ui.Label("Scrolling Frame Example", alignment=ui.Alignment.CENTER)
                            ui.Spacer(height=2)
                            ui.StringField()
                            ui.Spacer(height=5)
                            ui.ComboBox(0,"Dogs", "Are", "Awesome")
                            with ui.HStack():
                                # Create two checkboxes
                                ui.Label("Checkbox One")
                                ui.Spacer(width=4)
                                first = ui.CheckBox()
                            with ui.HStack():
                                ui.Label("Checkbox Two")
                                ui.Spacer(width=4)
                                second = ui.CheckBox()

                                # Connect one to another
                                first.model.add_value_changed_fn(
                                    lambda a, b=second: b.model.set_value(not a.get_value_as_bool()))
                                second.model.add_value_changed_fn(
                                    lambda a, b=first: b.model.set_value(not a.get_value_as_bool()))

                with ui.CanvasFrame():
                    with ui.VStack():
                        with ui.HStack():
                            ui.Label("Learn With Me is the Best Stream Ever!", alignment=ui.Alignment.CENTER)
                        with ui.VStack():
                            with ui.HStack():
                                ui.Button("Hello World", clicked_fn=self.on_click)
                                ui.Spacer(width=ui.Pixel(5))
                                ui.Button("Hello new button!", clicked_fn=self.on_newButton)
                        with ui.HStack():
                            first = ui.ProgressBar(style={"color": "green", "background_color": "cornflowerblue", "secondary_color": "pink"})
                            first.model.set_value(0.5)



    def on_click(self):
        print("hello world!")

    def on_newButton(self):
        print("hello new button!")

    def on_shutdown(self):
        print("[lwm.extension.ui] lwm extension ui shutdown")
