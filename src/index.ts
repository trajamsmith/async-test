import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './asynctest';

/**
 * Initialization data for the async_test extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'async-test',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension async-test is activated!');

    requestAPI<any>('get_example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The async_test server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default extension;
