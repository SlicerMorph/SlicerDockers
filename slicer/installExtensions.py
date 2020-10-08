extensionNames = ['MarkupsToModel', 'Auto3dgm', 'SegmentEditorExtraEffects', 'Sandbox', 'SlicerIGT', 'RawImageGuess', 'SlicerDcm2nii', 'SurfaceWrapSolidify', 'SlicerMorph']
em = slicer.app.extensionsManagerModel()

for extensionName in extensionNames:
  if not em.isExtensionInstalled(extensionName):
    extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)
    url = em.serverUrl().toString()+'/download/item/'+extensionMetaData['item_id']
    extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['md5']
    slicer.util.downloadFile(url, extensionPackageFilename)
    em.installExtension(extensionPackageFilename)

exit()