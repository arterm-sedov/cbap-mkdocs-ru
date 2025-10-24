#!/usr/bin/env python3
"""
MkDocs batch build script

This script sequentially builds MkDocs with the specified .yml configurations
and provides transparent terminal log output using Python's native logging module.

Features:
    - Real-time build output streaming
    - Build progress tracking and summary reporting

Usage:
    python build_pdf_guides.py

"""

import subprocess
import sys
import time
import logging
from datetime import datetime
from typing import Tuple


class MkDocsBatchBuilder:
    """
    MkDocs batch builder with transparent logging and error handling.
    
    This class manages the sequential building of multiple MkDocs configurations.
    
    Properties:
        configs (List[str]): List of MkDocs configuration files to build
        results (List[dict]): Build results for each configuration
        start_time (datetime): Timestamp when the build process started
        logger (logging.Logger): Configured logger instance
    """
    
    def __init__(self):
        """Initialize the batch builder with configuration files and logging setup."""
        # Configuration files to build in order
        self.configs = [
            "mkdocs_guide_complete_ru.yml",
            "mkdocs_guide_user_ru.yml",
            "mkdocs_guide_developer_ru_pdf.yml",
            "mkdocs_guide_admin_linux_ru_pdf.yml",
            "mkdocs_guide_admin_windows_ru_pdf.yml",
            "mkdocs_guide_api_ru_pdf.yml",
        ]
        self.results = []  # Store build results for summary
        self.start_time = datetime.now()  # Track total build time
        self._setup_logging()  # Configure Python native logging
        
    def _setup_logging(self) -> None:
        """
        Setup Python native logging configuration.
        
        Configures a dedicated logger with both console and file output,
        using the same formatter for consistent logging.
        """
        # Create dedicated logger instance
        self.logger = logging.getLogger('MkDocsBatchBuilder')
        self.logger.setLevel(logging.INFO)
        
        # Create formatter for consistent output
        formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # Console handler for real-time output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        # File handler for persistent log
        file_handler = logging.FileHandler('build_log.txt', mode='w', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        
        # Add both handlers to logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        
        # Prevent duplicate logs from propagating to root logger
        self.logger.propagate = False
        
        
    def build_config(self, config_file: str) -> Tuple[bool, str, float]:
        """
        Build a single MkDocs configuration with real-time output streaming.
        
        Args:
            config_file (str): Path to the MkDocs configuration file
            
        Returns:
            Tuple[bool, str, float]: (success, output, duration)
                - success: True if build succeeded, False otherwise
                - output: Complete build output as string
                - duration: Build time in seconds
        """
        self.logger.info(f"Building {config_file}...")
        start_time = time.time()
        
        try:
            # Launch MkDocs build process with output capture
            process = subprocess.Popen(
                [sys.executable, "-m", "mkdocs", "build", "-f", config_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # Redirect stderr to stdout for unified output
                universal_newlines=True,
                bufsize=1  # Line buffered for real-time streaming
            )
            
            # Stream build output in real-time while capturing for summary
            output_lines = []
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())  # Real-time terminal output
                    output_lines.append(output.strip())  # Capture for logging
                    
            return_code = process.poll()
            duration = time.time() - start_time
            
            # Log build result with timing information
            if return_code == 0:
                self.logger.info(f"Successfully built {config_file} in {duration:.2f}s")
                return True, "\n".join(output_lines), duration
            else:
                self.logger.error(f"Failed to build {config_file} (exit code: {return_code})")
                return False, "\n".join(output_lines), duration
                
        except Exception as e:
            # Handle unexpected exceptions during build process
            duration = time.time() - start_time
            error_msg = f"Exception while building {config_file}: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg, duration
            
    def build_all(self) -> bool:
        """
        Build all configurations sequentially with progress tracking.
        
        Processes each configuration file in order, collecting results
        and continuing even if individual builds fail.
        
        Returns:
            bool: True if all builds succeeded, False if any failed
        """
        self.logger.info("Starting sequential build process...")
        self.logger.info(f"Total configurations to build: {len(self.configs)}")
        
        all_successful = True
        
        # Process each configuration sequentially
        for i, config in enumerate(self.configs, 1):
            self.logger.info(f"Progress: {i}/{len(self.configs)} - Processing {config}")
            
            # Build current configuration and capture results
            success, output, duration = self.build_config(config)
            
            # Store build result for summary reporting
            result = {
                'config': config,
                'success': success,
                'duration': duration,
                'output': output
            }
            self.results.append(result)
            
            # Handle build failures gracefully
            if not success:
                all_successful = False
                self.logger.warning(f"Build failed for {config}. Continuing with next configuration...")
            else:
                self.logger.info(f"Build completed for {config}")
                
            # Add visual separator between builds (except for last one)
            if i < len(self.configs):
                self.logger.info("-" * 60)
                
        return all_successful
        
    def print_summary(self) -> None:
        """
        Print build summary with statistics and detailed results.
        
        Displays:
            - Total build time and configuration count
            - Success/failure statistics
            - Individual build results with timing
            - List of failed configurations (if any)
        """
        total_duration = (datetime.now() - self.start_time).total_seconds()
        
        # Print summary header
        self.logger.info("=" * 80)
        self.logger.info("BUILD SUMMARY")
        self.logger.info("=" * 80)
        
        # Calculate success/failure statistics
        successful = sum(1 for r in self.results if r['success'])
        failed = len(self.results) - successful
        
        # Display overall statistics
        self.logger.info(f"Total configurations: {len(self.results)}")
        self.logger.info(f"Successful builds: {successful}")
        self.logger.info(f"Failed builds: {failed}")
        self.logger.info(f"Total time: {total_duration:.2f}s")
        
        # Display detailed results for each configuration
        self.logger.info("\nDetailed Results:")
        self.logger.info("-" * 40)
        
        for result in self.results:
            status = "✓ SUCCESS" if result['success'] else "✗ FAILED"
            self.logger.info(f"{result['config']}: {status} ({result['duration']:.2f}s)")
            
        # List failed configurations if any
        if failed > 0:
            self.logger.info(f"\nFailed configurations:")
            for result in self.results:
                if not result['success']:
                    self.logger.info(f"  - {result['config']}")
                    
        self.logger.info("=" * 80)
        
    def run(self) -> int:
        """
        Main execution method orchestrating the entire build process.
        
        Executes the complete workflow:
            1. Build all configurations sequentially
            2. Generate summary report
            
        Returns:
            int: Exit code (0 for success, 1 for failure)
        """
        self.logger.info("MkDocs batch builder")
        self.logger.info("=" * 60)
        
        # Execute sequential build process for all configurations
        success = self.build_all()
        
        # Generate and display build summary
        self.print_summary()
        
        # Return appropriate exit code based on overall success
        return 0 if success else 1


def main():
    """
    Main entry point for the MkDocs batch build script.
    
    Creates a MkDocsBatchBuilder instance and executes the complete
    build process, returning the appropriate exit code.
    """
    builder = MkDocsBatchBuilder()
    exit_code = builder.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
