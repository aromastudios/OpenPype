from pyblish import api
import os


class CollectReviews(api.InstancePlugin):
    """Collect review from tags.

    Tag is expected to have metadata:
        {
            "family": "review"
            "track": "trackName"
        }
    """

    # Run just before CollectSubsets
    order = api.CollectorOrder + 0.1022
    label = "Collect Reviews"
    hosts = ["nukestudio"]
    families = ["clip"]

    def process(self, instance):
        # Exclude non-tagged instances.
        tagged = False
        for tag in instance.data["tags"]:
            family = dict(tag["metadata"]).get("tag.family", "")
            if family.lower() == "review":
                tagged = True
                track = dict(tag["metadata"]).get("tag.track")
                break

        if not tagged:
            self.log.debug(
                "Skipping \"{}\" because its not tagged with "
                "\"review\"".format(instance)
            )
            return

        if not track:
            self.log.debug(
                "Skipping \"{}\" because tag is not having `track` in metadata".format(instance)
            )
            return

        # add to representations
        if not instance.data.get("representations"):
            instance.data["representations"] = list()

        if track in instance.data["track"]:
            self.log.debug("Review will work on `subset`: {}".format(
                instance.data["subset"]))

            # change families
            instance.data["family"] = "plate"
            instance.data["families"] = ["review", "ftrack"]

            self.version_data(instance)
            self.create_thumbnail(instance)

            rev_inst = instance

        else:
            self.log.debug("Track item on plateMain")
            rev_inst = None
            for inst in instance.context[:]:
                if inst.data["track"] in track:
                    rev_inst = inst
                    self.log.debug("Instance review: {}".format(
                        rev_inst.data["name"]))

            if rev_inst is None:
                raise RuntimeError(
                    "TrackItem from track name `{}` has to be also selected".format(
                        track)
                )
            instance.data["families"].append("review")

        file_path = rev_inst.data.get("sourcePath")
        file_dir = os.path.dirname(file_path)
        file = os.path.basename(file_path)
        ext = os.path.splitext(file)[-1][1:]

        # change label
        instance.data["label"] = "{0} - {1} - ({2}) - review".format(
            instance.data['asset'], instance.data["subset"], ext
        )

        self.log.debug("Instance review: {}".format(rev_inst.data["name"]))


        # adding representation for review mov
        representation = {
            "files": file,
            "stagingDir": file_dir,
            "startFrame": rev_inst.data.get("sourceIn"),
            "endFrame": rev_inst.data.get("sourceOut"),
            "step": 1,
            "frameRate": rev_inst.data.get("fps"),
            "preview": True,
            "thumbnail": False,
            "name": "preview",
            "ext": ext
        }
        instance.data["representations"].append(representation)

        self.log.debug("Added representation: {}".format(representation))

    def create_thumbnail(self, instance):
        item = instance.data["item"]
        source_in = instance.data["sourceIn"]

        source_path = instance.data["sourcePath"]
        source_file = os.path.basename(source_path)
        head, ext = os.path.splitext(source_file)

        # staging dir creation
        staging_dir = os.path.dirname(
            source_path)

        thumb_file = head + ".png"
        thumb_path = os.path.join(staging_dir, thumb_file)
        self.log.debug("__ thumb_path: {}".format(thumb_path))
        self.log.debug("__ source_in: {}".format(source_in))
        thumbnail = item.thumbnail(source_in).save(
            thumb_path,
            format='png'
        )
        self.log.debug("__ thumbnail: {}".format(thumbnail))

        thumb_representation = {
            'files': thumb_file,
            'stagingDir': staging_dir,
            'name': "thumbnail",
            'thumbnail': True,
            'ext': "png"
        }
        instance.data["representations"].append(
            thumb_representation)

    def version_data(self, instance):
        item = instance.data["item"]

        transfer_data = [
            "handleStart", "handleEnd", "sourceIn", "sourceOut", "startFrame", "endFrame", "sourceInH", "sourceOutH", "timelineIn", "timelineOut", "timelineInH", "timelineOutH", "asset", "track", "version"
        ]

        version_data = dict()
        # pass data to version
        version_data.update({k: instance.data[k] for k in transfer_data})

        # add to data of representation
        version_data.update({
            "handles": version_data['handleStart'],
            "colorspace": item.sourceMediaColourTransform(),
            "families": instance.data["families"],
            "subset": instance.data["subset"],
            "fps": instance.context.data["fps"]
        })
        instance.data["versionData"] = version_data

        instance.data["source"] = instance.data["sourcePath"]
