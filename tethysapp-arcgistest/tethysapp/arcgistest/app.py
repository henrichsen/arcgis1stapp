from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgistest(TethysAppBase):
    """
    Tethys app class for Arc Gis Test App.
    """

    name = 'Arc Gis Test App'
    index = 'arcgistest:home'
    icon = 'arcgistest/images/icon.gif'
    package = 'arcgistest'
    root_url = 'arcgistest'
    color = '#27ae60'
    description = 'This is a test arcGis that has a picture of a cute dino on the front. what else do you need?'
    tags = 'cute, dino, first app, arcgis'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='arcgistest',
                controller='arcgistest.controllers.home'
            ),
            UrlMap(
                name='motus',
                url='arcgistest/motus',
                controller='arcgistest.controllers.motus'
            ),
        )

        return url_maps
